import re

with open('player/relatorio-empreendimento-europark-noronha-ins-2026-016-1772053379394.html', 'r', encoding='utf-8') as f:
    source = f.read()

with open('laudo-elevadores-pericia-tecnica.html', 'r', encoding='utf-8') as f:
    dashboard = f.read()

# Find Torre C1 Social 3-4 in source and get video
torre_c1_idx = source.find('Torre C1 - Elevador Social 3-4')
chunk_after = source[torre_c1_idx:torre_c1_idx+5000]
video_ids = re.findall(r'youtube\.com/embed/([a-zA-Z0-9_-]+)', chunk_after)
print('Video IDs found after Torre C1 in source:', video_ids[:3])

# Get all SVGs in source with positions
svgs_source = [(m.start(), m.group(0)) for m in re.finditer(r'<svg viewBox="0 0 820.*?</svg>', source, re.DOTALL)]
print(f'Total SVGs in source: {len(svgs_source)}')

# Also check what's in the dashboard
video_id_dash = re.findall(r'youtube\.com/embed/([a-zA-Z0-9_-]+)', dashboard)
print('Video ID in dashboard:', video_id_dash)

# Print context around Torre C1 to find the section
torre_c1_positions = [(m.start()) for m in re.finditer(r'Torre C1 - Elevador Social 3-4', source)]
print('Positions of Torre C1:', torre_c1_positions)

# Check elevator order of the h2 elements
elevators = re.findall(r'<h2 class="elevator-title">(.*?)</h2>', source)
for i, e in enumerate(elevators):
    print(f'Elevator {i}: {e}')
