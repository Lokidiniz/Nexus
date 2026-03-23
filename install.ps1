# NEXUS v2.0 — Installer for Windows (PowerShell)
# Usage: irm <url>/install.ps1 | iex

$RepoUrl = "https://raw.githubusercontent.com/Lokidiniz/Nexus/main"
$ClaudeDir = "$env:USERPROFILE\.claude"
$AgentsDir = "$ClaudeDir\agents"
$SkillsDir = "$ClaudeDir\skills"

Write-Host ""
Write-Host "╔══════════════════════════════════════════════════════════════╗"
Write-Host "║   NEXUS v2.0 — Academic Research Squad Installer            ║"
Write-Host "║   PT-BR · EN · ES  │  Claude Code                          ║"
Write-Host "╚══════════════════════════════════════════════════════════════╝"
Write-Host ""

# Check Claude Code installation
if (-not (Test-Path $ClaudeDir)) {
    Write-Host "❌ Claude Code directory not found at $ClaudeDir"
    Write-Host "   Please install Claude Code first: https://claude.ai/code"
    exit 1
}

# Create directories if needed
@($AgentsDir, "$SkillsDir\nexus", "$SkillsDir\nexus-en", "$SkillsDir\nexus-es") | ForEach-Object {
    if (-not (Test-Path $_)) { New-Item -ItemType Directory -Path $_ -Force | Out-Null }
}

Write-Host "📦 Installing NEXUS agents..."

$Agents = @(
    "nexus.md",
    "literature-researcher.md",
    "methodologist.md",
    "critical-analyst.md",
    "scientific-writer.md",
    "peer-reviewer.md",
    "data-specialist.md"
)

foreach ($agent in $Agents) {
    Write-Host "   → $agent"
    Invoke-WebRequest -Uri "$RepoUrl/agents/$agent" -OutFile "$AgentsDir\$agent" -UseBasicParsing
}

Write-Host ""
Write-Host "📦 Installing NEXUS skills..."

$Skills = @("nexus", "nexus-en", "nexus-es")
foreach ($skill in $Skills) {
    Write-Host "   → skill: $skill"
    Invoke-WebRequest -Uri "$RepoUrl/skills/$skill/SKILL.md" -OutFile "$SkillsDir\$skill\SKILL.md" -UseBasicParsing
}

Write-Host ""
Write-Host "✅ NEXUS v2.0 installed successfully!"
Write-Host ""
Write-Host "Usage in Claude Code:"
Write-Host "   /nexus          — auto-detect language (PT-BR/EN/ES)"
Write-Host "   /nexus-en       — English mode"
Write-Host "   /nexus-es       — Español mode"
Write-Host ""
Write-Host "Example:"
Write-Host "   /nexus revisão de literatura sobre sensores eletroquímicos com MOFs"
Write-Host ""
