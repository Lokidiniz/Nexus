#!/usr/bin/env node

/**
 * NEXUS Academic Research Framework
 * npx nexus-research init
 *
 * Installs NEXUS agents, workflows, tasks, and teams into the current directory.
 * No dependencies — pure Node.js built-ins only.
 */

const https = require('https');
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// ─── Config ──────────────────────────────────────────────────────────────────

const REPO = 'Lokidiniz/Nexus';
const BRANCH = 'main';
const BASE_URL = `https://raw.githubusercontent.com/${REPO}/${BRANCH}`;
const REPO_URL = `https://github.com/${REPO}`;

const VERSION = '3.0.0';

// ─── Colors ──────────────────────────────────────────────────────────────────

const c = {
  reset: '\x1b[0m',
  bold:  '\x1b[1m',
  dim:   '\x1b[2m',
  green: '\x1b[32m',
  cyan:  '\x1b[36m',
  yellow:'\x1b[33m',
  red:   '\x1b[31m',
  purple:'\x1b[35m',
};

const bold   = s => `${c.bold}${s}${c.reset}`;
const green  = s => `${c.green}${s}${c.reset}`;
const cyan   = s => `${c.cyan}${s}${c.reset}`;
const yellow = s => `${c.yellow}${s}${c.reset}`;
const red    = s => `${c.red}${s}${c.reset}`;
const dim    = s => `${c.dim}${s}${c.reset}`;
const purple = s => `${c.purple}${s}${c.reset}`;

// ─── Files to install ────────────────────────────────────────────────────────

const FILES = {
  agents: [
    'agents/nexus.md',
    'agents/literature-researcher.md',
    'agents/methodologist.md',
    'agents/critical-analyst.md',
    'agents/scientific-writer.md',
    'agents/peer-reviewer.md',
    'agents/data-specialist.md',
  ],
  workflows: [
    'workflows/literature-review.yaml',
    'workflows/full-manuscript.yaml',
    'workflows/pre-submission.yaml',
    'workflows/funding-proposal.yaml',
    'workflows/thesis.yaml',
    'workflows/data-analysis.yaml',
    'workflows/rebuttal.yaml',
    'workflows/poster.yaml',
  ],
  tasks: [
    'tasks/search-literature.md',
    'tasks/write-section.md',
    'tasks/calculate-lod.md',
    'tasks/design-study.md',
    'tasks/review-manuscript.md',
    'tasks/write-rebuttal.md',
    'tasks/write-abstract.md',
    'tasks/plan-figures.md',
    'tasks/write-cover-letter.md',
  ],
  teams: [
    'teams/team-electrochemistry.yaml',
    'teams/team-education.yaml',
    'teams/team-health.yaml',
    'teams/team-social-sciences.yaml',
  ],
  nexus: [
    '.nexus/constitution.md',
    '.nexus/activation-pipeline.md',
    '.nexus/rds.md',
  ],
  claude: [
    '.claude/CLAUDE.md',
    '.claude/settings.json',
  ],
  hooks: [
    '.nexus/hooks/reference-guard.py',
    '.nexus/hooks/constitution-enforcer.py',
  ],
  root: [
    'CLAUDE.md',
  ],
};

// ─── Helpers ─────────────────────────────────────────────────────────────────

function fetch(url) {
  return new Promise((resolve, reject) => {
    https.get(url, res => {
      if (res.statusCode === 301 || res.statusCode === 302) {
        return fetch(res.headers.location).then(resolve).catch(reject);
      }
      if (res.statusCode !== 200) {
        return reject(new Error(`HTTP ${res.statusCode} — ${url}`));
      }
      const chunks = [];
      res.on('data', c => chunks.push(c));
      res.on('end', () => resolve(Buffer.concat(chunks).toString('utf8')));
      res.on('error', reject);
    }).on('error', reject);
  });
}

function ensureDir(p) {
  if (!fs.existsSync(p)) fs.mkdirSync(p, { recursive: true });
}

function writeFile(dest, content) {
  ensureDir(path.dirname(dest));
  fs.writeFileSync(dest, content, 'utf8');
}

async function installFile(relPath, destDir, overwrite) {
  const dest = path.join(destDir, relPath);

  if (fs.existsSync(dest) && !overwrite) {
    return 'skipped';
  }

  const url = `${BASE_URL}/${relPath}`;
  const content = await fetch(url);
  writeFile(dest, content);
  return 'installed';
}

function detectClaude() {
  const home = process.env.HOME || process.env.USERPROFILE || '';
  const win  = path.join(home, '.claude');
  const unix = path.join(home, '.claude');
  return fs.existsSync(win) ? win : fs.existsSync(unix) ? unix : null;
}

function prompt(question) {
  process.stdout.write(question);
  const buf = Buffer.alloc(1024);
  let len;
  try {
    len = fs.readSync(0, buf, 0, 1024, null);
  } catch {
    return '';
  }
  return buf.slice(0, len).toString('utf8').trim();
}

// ─── CLI args ────────────────────────────────────────────────────────────────

const args = process.argv.slice(2);
const command = args[0] || 'init';
const flags = {
  yes:      args.includes('--yes') || args.includes('-y'),
  force:    args.includes('--force') || args.includes('-f'),
  global:   args.includes('--global') || args.includes('-g'),
  noHooks:  args.includes('--no-hooks'),
  noIde:    args.includes('--no-ide'),
};

// ─── Banner ──────────────────────────────────────────────────────────────────

function printBanner() {
  console.log('');
  console.log(purple('╔══════════════════════════════════════════════════════════════════╗'));
  console.log(purple('║') + bold(`   NEXUS v${VERSION}  │  Academic Research Squad  │  PT-BR · EN · ES    `) + purple('║'));
  console.log(purple('║') + dim('   "We return control to those with the courage to build."        ') + purple('║'));
  console.log(purple('╚══════════════════════════════════════════════════════════════════╝'));
  console.log('');
}

// ─── Commands ────────────────────────────────────────────────────────────────

async function cmdInit() {
  printBanner();
  console.log(bold('Installing NEXUS Academic Research Framework...'));
  console.log('');

  const cwd = process.cwd();
  const claudeDir = detectClaude();

  // Determine install targets
  const installLocal = !flags.global;
  const installGlobal = flags.global || !!claudeDir;

  console.log(`  ${dim('Project directory:')} ${cwd}`);
  if (claudeDir) console.log(`  ${dim('Claude Code agents:')} ${claudeDir}/agents`);
  console.log('');

  if (!flags.yes) {
    const confirm = prompt(`Install NEXUS here? [Y/n] `);
    if (confirm.toLowerCase() === 'n') {
      console.log(yellow('Aborted.'));
      process.exit(0);
    }
  }

  console.log('');

  let installed = 0;
  let skipped = 0;
  let errors = 0;

  // Install all file groups
  const allGroups = { ...FILES };
  if (flags.noHooks) delete allGroups.hooks;

  for (const [group, files] of Object.entries(allGroups)) {
    process.stdout.write(`  ${cyan('→')} Installing ${group}... `);
    let groupInstalled = 0;

    for (const file of files) {
      try {
        const result = await installFile(file, cwd, flags.force);
        if (result === 'installed') { installed++; groupInstalled++; }
        else skipped++;
      } catch (err) {
        errors++;
        // Non-fatal: some files may not exist yet in the repo
      }
    }

    console.log(green(`✓`) + ` (${groupInstalled} files)`);
  }

  // Install agents to Claude Code global dir
  if (claudeDir && !flags.noIde) {
    process.stdout.write(`  ${cyan('→')} Installing agents to Claude Code... `);
    let agentCount = 0;

    for (const file of FILES.agents) {
      const dest = path.join(claudeDir, file);
      const src  = path.join(cwd, file);

      if (fs.existsSync(src) && (!fs.existsSync(dest) || flags.force)) {
        ensureDir(path.dirname(dest));
        fs.copyFileSync(src, dest);
        agentCount++;
      }
    }

    // Copy CLAUDE.md to user's global .claude
    const globalClaudeMd = path.join(claudeDir, 'CLAUDE.md');
    const localClaudeMd  = path.join(cwd, 'CLAUDE.md');
    if (fs.existsSync(localClaudeMd) && (!fs.existsSync(globalClaudeMd) || flags.force)) {
      fs.copyFileSync(localClaudeMd, globalClaudeMd);
    }

    console.log(green('✓') + ` (${agentCount} agents)`);
  }

  // Summary
  console.log('');
  console.log(green('✓') + bold(` NEXUS installed successfully!`));
  console.log('');
  console.log('  Next steps:');
  console.log(`    1. Open this folder in ${bold('Claude Code')}`);
  console.log(`    2. Type ${bold('*pipeline literature-review')} to start`);
  console.log(`    3. Or ask ${bold('*quick [your question]')} for a fast answer`);
  console.log('');
  console.log(`  ${dim('Documentation:')} ${REPO_URL}`);
  console.log(`  ${dim('Issues:')}        ${REPO_URL}/issues`);
  console.log('');
}

function cmdHelp() {
  printBanner();
  console.log(bold('Usage:'));
  console.log('  npx nexus-research init          Install NEXUS in current directory');
  console.log('  npx nexus-research init --force  Overwrite existing files');
  console.log('  npx nexus-research init --global Install agents globally');
  console.log('  npx nexus-research init --yes    Skip confirmation prompt');
  console.log('  npx nexus-research version       Show version');
  console.log('  npx nexus-research help          Show this message');
  console.log('');
  console.log(bold('Pipelines (after install, inside Claude Code):'));
  console.log('  *pipeline literature-review    Systematic literature review');
  console.log('  *pipeline full-manuscript      Full paper from scratch');
  console.log('  *pipeline pre-submission       Review before submitting');
  console.log('  *pipeline data-analysis        Analyze your data');
  console.log('  *pipeline funding-proposal     CNPq / CAPES / NSF proposal');
  console.log('  *pipeline thesis               Thesis chapter');
  console.log('  *pipeline rebuttal             Respond to reviewers');
  console.log('  *pipeline poster               Scientific poster');
  console.log('');
}

function cmdVersion() {
  console.log(`nexus-research v${VERSION}`);
}

// ─── Main ────────────────────────────────────────────────────────────────────

(async () => {
  try {
    switch (command) {
      case 'init':    await cmdInit(); break;
      case 'help':    cmdHelp(); break;
      case 'version': cmdVersion(); break;
      default:
        console.error(red(`Unknown command: ${command}`));
        console.error('Run: npx nexus-research help');
        process.exit(1);
    }
  } catch (err) {
    console.error('');
    console.error(red('Error: ') + err.message);
    process.exit(1);
  }
})();
