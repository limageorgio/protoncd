$root = 'd:\apps\protoncd-1'
Set-Location $root
git add CHECKLIST-INDEXACAO-DOMINIO.md
git commit -m "docs: update indexation checklist - canonical URLs fixed (135 files, 100 percent success)"
git push origin main
Write-Output "Commit realizado com sucesso"
