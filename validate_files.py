#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validate the new and updated files for syntax errors.
"""

import os
import json
from html.parser import HTMLParser

os.chdir("h:\\apps\\protoncd")

validation_results = {
    'html_files': {},
    'json_files': {},
    'errors': [],
    'warnings': []
}

# List of new HTML files to validate
html_files = [
    "artigos/elevadores/artigo-elevadores-visor-vidro-porta-pavimento.html",
    "artigos/elevadores/artigo-elevadores-piso-cabina-liso.html",
    "artigos/elevadores/artigo-elevadores-para-choques-buffers-ressecados.html",
    "artigos/elevadores/artigo-elevadores-corrimao-cabina-padrao.html",
    "artigos/elevadores/artigo-elevadores-assento-basculante-acessibilidade.html",
    "artigos/elevadores/artigo-elevadores-iluminacao-emergencia-cabina.html",
    "artigos/elevadores/artigo-elevadores-sensor-porta-deteccao-pessoa.html",
    "artigos/elevadores/artigo-elevadores-vibracao-lateral-excessiva.html",
    "artigos/elevadores/artigo-elevadores-fiacao-conectores-expostos-quadro.html",
    "artigos/elevadores/artigo-elevadores-aterramento-inadequado-elevador.html",
]

# Updated files to validate
updated_files = [
    "artigos/elevadores/index.html",
    "conhecimento-tecnico/index.html",
    "conhecimento-tecnico/dados/elevadores.json",
]

print("=" * 60)
print("VALIDATING NEW HTML ARTICLE FILES")
print("=" * 60)

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Basic checks
        if not content.strip().startswith('<!DOCTYPE'):
            validation_results['warnings'].append(f"{filepath}: Does not start with DOCTYPE")
        
        if content.count('<html') != content.count('</html>'):
            validation_results['errors'].append(f"{filepath}: Mismatched html tags")
        
        if content.count('<body') != content.count('</body>'):
            validation_results['errors'].append(f"{filepath}: Mismatched body tags")
        
        # Check for required meta tags
        required_tags = ['<meta charset', '<title>', '<link rel="canonical"']
        for tag in required_tags:
            if tag not in content.lower():
                validation_results['warnings'].append(f"{filepath}: Missing {tag}")
        
        # Check for CTAs
        if 'WhatsApp' not in content and 'whatsapp' not in content.lower():
            validation_results['warnings'].append(f"{filepath}: Missing WhatsApp CTA")
        
        validation_results['html_files'][filepath] = 'VALID ✓'
        print(f"✓ {os.path.basename(filepath)}")
        
    except Exception as e:
        validation_results['errors'].append(f"{filepath}: {str(e)}")
        validation_results['html_files'][filepath] = f'ERROR: {str(e)}'
        print(f"✗ {os.path.basename(filepath)}: {str(e)}")

print("\n" + "=" * 60)
print("VALIDATING UPDATED FILES")
print("=" * 60)

# Validate JSON files
for filepath in [updated_files[2]]:  # Just the JSON file
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Check structure
        if 'categoria' not in data or 'faqs' not in data:
            validation_results['errors'].append(f"{filepath}: Missing required JSON structure")
        
        # Check that elev-063 to elev-072 have artigo_relacionado
        for faq in data['faqs']:
            if 63 <= int(faq.get('id', 'elev-000').split('-')[1]) <= 72:
                if 'artigo_relacionado' not in faq:
                    validation_results['errors'].append(f"{filepath}: {faq.get('id')} missing artigo_relacionado")
        
        validation_results['json_files'][filepath] = 'VALID ✓'
        print(f"✓ {os.path.basename(filepath)}")
        
    except json.JSONDecodeError as e:
        validation_results['errors'].append(f"{filepath}: JSON parse error: {str(e)}")
        validation_results['json_files'][filepath] = f'ERROR: {str(e)}'
        print(f"✗ {os.path.basename(filepath)}: {str(e)}")
    except Exception as e:
        validation_results['errors'].append(f"{filepath}: {str(e)}")
        validation_results['json_files'][filepath] = f'ERROR: {str(e)}'
        print(f"✗ {os.path.basename(filepath)}: {str(e)}")

# Validate HTML files that were updated
for filepath in [updated_files[0], updated_files[1]]:  # index files
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Basic checks
        if content.count('<') != content.count('>'):
            validation_results['warnings'].append(f"{filepath}: Possible tag mismatch")
        
        # Check for required content
        if 'elev-063' not in content:
            validation_results['errors'].append(f"{filepath}: Missing elev-063 reference")
        if 'elev-072' not in content:
            validation_results['errors'].append(f"{filepath}: Missing elev-072 reference")
        
        validation_results['html_files'][filepath] = 'VALID ✓'
        print(f"✓ {os.path.basename(filepath)}")
        
    except Exception as e:
        validation_results['errors'].append(f"{filepath}: {str(e)}")
        validation_results['html_files'][filepath] = f'ERROR: {str(e)}'
        print(f"✗ {os.path.basename(filepath)}: {str(e)}")

print("\n" + "=" * 60)
print("VALIDATION SUMMARY")
print("=" * 60)

total_valid = len(validation_results['html_files']) + len(validation_results['json_files'])
total_errors = len(validation_results['errors'])
total_warnings = len(validation_results['warnings'])

print(f"Total files validated: {total_valid}")
print(f"Errors found: {total_errors}")
print(f"Warnings found: {total_warnings}")

if total_errors > 0:
    print("\n⚠ ERRORS:")
    for error in validation_results['errors']:
        print(f"  - {error}")

if total_warnings > 0:
    print("\n⚠ WARNINGS:")
    for warning in validation_results['warnings']:
        print(f"  - {warning}")

if total_errors == 0:
    print("\n✓ ALL VALIDATIONS PASSED!")
else:
    print("\n✗ Some validations failed - please review")
