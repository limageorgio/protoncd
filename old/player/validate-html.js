#!/usr/bin/env node
/**
 * VALIDADOR DE HTML - Versão JavaScript
 * Arquivo de exemplo para usar em Node.js ou navegador
 * 
 * Node.js: node validate-html.js arquivo.html
 * Navegador: Copie a função validateHTMLContent para usar em admin.html
 */

/**
 * Validar conteúdo HTML procurando por padrões verdadeiramente perigosos
 */
function validateHTMLContent(content) {
    // Padrões verdadeiramente perigosos que devemos bloquear
    const dangerous_patterns = [
        /<script[^>]*src\s*=\s*["'](?:javascript:|data:|about:)/i,  // Scripts com protocolos perigosos
        /<script[^>]*>\s*eval\s*\(/i,                                // eval() direto
        /<script[^>]*>\s*document\.write\s*\(/i,                     // document.write suspeito
        /<?php/i,                                                     // PHP tags
        /<%[^=]/i,                                                    // ASP tags (permite <%=)
        /<script[^>]*>\s*window\.location/i,                         // Redirecionamento suspeito
        /<script[^>]*>\s*location\.href/i,                           // Redirecionamento suspeito
        /<meta[^>]*http-equiv\s*=\s*["']refresh["'][^>]*url=/i,     // Meta refresh com URL
    ];

    const patternNames = [
        'Script com protocolo perigoso (javascript:, data:, about:)',
        'Uso de eval() detectado',
        'document.write() suspeito',
        'PHP tags',
        'ASP tags',
        'Redirecionamento window.location',
        'Redirecionamento location.href',
        'Meta refresh com URL'
    ];

    for (let i = 0; i < dangerous_patterns.length; i++) {
        if (dangerous_patterns[i].test(content)) {
            return { valid: false, error: patternNames[i] + ' detectado' };
        }
    }

    // Verificar se é HTML válido (básico)
    if (!/<html/i.test(content) && !/<body/i.test(content) && !/<head/i.test(content) && !/<!DOCTYPE/i.test(content)) {
        return { valid: false, error: 'Não parece ser um arquivo HTML válido' };
    }

    return { valid: true, error: null };
}

/**
 * Verificar arquivo
 */
function validateFile(filename, content) {
    console.log('\n╔════════════════════════════════════════════════════════╗');
    console.log('║  VALIDADOR DE HTML - JavaScript                        ║');
    console.log('╚════════════════════════════════════════════════════════╝\n');

    // Verificar extensão
    if (!filename.toLowerCase().endsWith('.html')) {
        console.log('❌ FALHOU: Apenas arquivos .html são permitidos');
        return false;
    }

    console.log('📋 Validando:', filename);
    console.log('📊 Tamanho:', (content.length / 1024).toFixed(2) + ' KB\n');

    // Validações
    const validations = [];

    // 1. Scripts
    const hasScripts = /<script[^>]*>.*?<\/script>/is.test(content);
    validations.push({
        name: 'Scripts inline',
        valid: !hasScripts,
        msg: hasScripts ? 'Scripts detectados' : 'Sem scripts inline'
    });

    // 2. JavaScript protocol
    const hasJSProtocol = /javascript:/i.test(content);
    validations.push({
        name: 'JavaScript protocol',
        valid: !hasJSProtocol,
        msg: hasJSProtocol ? 'javascript: detectado' : 'Sem javascript: protocol'
    });

    // 3. Event handlers
    const hasHandlers = /on\w+\s*=/i.test(content);
    validations.push({
        name: 'Event handlers',
        valid: !hasHandlers,
        msg: hasHandlers ? 'Event handlers detectados' : 'Sem event handlers'
    });

    // 4. iframes
    const hasIframes = /<iframe[^>]*>/i.test(content);
    validations.push({
        name: 'iframes',
        valid: !hasIframes,
        msg: hasIframes ? 'iframes detectados' : 'Sem iframes'
    });

    // 5. Objects
    const hasObjects = /<object[^>]*>/i.test(content);
    validations.push({
        name: 'Objects',
        valid: !hasObjects,
        msg: hasObjects ? 'Objects detectados' : 'Sem objects'
    });

    // 6. Embeds
    const hasEmbeds = /<embed[^>]*>/i.test(content);
    validations.push({
        name: 'Embeds',
        valid: !hasEmbeds,
        msg: hasEmbeds ? 'Embeds detectados' : 'Sem embeds'
    });

    // 7. PHP/ASP
    const hasServerCode = /<?php|<%/i.test(content);
    validations.push({
        name: 'Código de servidor',
        valid: !hasServerCode,
        msg: hasServerCode ? 'Código de servidor detectado' : 'Sem código de servidor'
    });

    // 8. Estrutura HTML
    const isValidHTML = /<html/i.test(content) || /<body/i.test(content) || /<!/i.test(content);
    validations.push({
        name: 'Estrutura HTML válida',
        valid: isValidHTML,
        msg: isValidHTML ? 'HTML válido' : 'HTML básico'
    });

    // Exibir resultados
    console.log('📊 RESULTADOS DAS VALIDAÇÕES:\n');

    let passedCount = 0;
    for (let v of validations) {
        const status = v.valid ? '✅' : '⚠️';
        console.log(`${status} ${v.name.padEnd(30)} → ${v.msg}`);
        if (v.valid) passedCount++;
    }

    console.log('\n════════════════════════════════════════════════════════\n');

    const total = validations.length;
    const percentage = Math.round((passedCount / total) * 100);

    if (passedCount === total) {
        console.log('✅ RESULTADO: ARQUIVO PASSOU EM TODAS AS VALIDAÇÕES\n');
        console.log('Este arquivo é seguro para fazer upload.\n');
        return true;
    } else {
        console.log(`⚠️  RESULTADO: ${passedCount}/${total} validações passaram (${percentage}%)\n`);
        console.log('Problemas encontrados:\n');

        for (let v of validations) {
            if (!v.valid) {
                console.log(`- ${v.msg}`);
            }
        }

        console.log('\nResolva os problemas acima antes de fazer upload.\n');
        return false;
    }
}

// ========================================
// EXECUTAR EM NODE.JS
// ========================================

// Verificar se é executado em Node.js
if (typeof module !== 'undefined' && module.exports) {
    const fs = require('fs');
    const path = require('path');

    // Verificar argumentos
    if (process.argv.length < 3) {
        console.log('Uso: node validate-html.js <arquivo.html>');
        console.log('Exemplo: node validate-html.js meu-player.html\n');
        process.exit(1);
    }

    const filePath = process.argv[2];

    // Verificar se arquivo existe
    if (!fs.existsSync(filePath)) {
        console.log('❌ ERRO: Arquivo não encontrado: ' + filePath + '\n');
        process.exit(1);
    }

    // Ler arquivo
    try {
        const content = fs.readFileSync(filePath, 'utf-8');
        const filename = path.basename(filePath);
        const result = validateFile(filename, content);
        process.exit(result ? 0 : 1);
    } catch (error) {
        console.log('❌ ERRO: Não foi possível ler o arquivo\n');
        console.log('Erro: ' + error.message + '\n');
        process.exit(1);
    }
}

// ========================================
// EXPORTAR PARA NAVEGADOR
// ========================================

if (typeof window !== 'undefined') {
    window.validateHTMLContent = validateHTMLContent;
    window.validateFile = validateFile;
}

// ========================================
// EXPORTAR PARA MODULE.EXPORTS
// ========================================

if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        validateHTMLContent,
        validateFile
    };
}
