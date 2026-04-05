# AGENTS.md

Operating guide for agentic coding assistants in `2025-blog-public`.

## 1) Repository Facts

- Stack: Next.js 16, React 19, TypeScript 5.
- Package manager: `pnpm` (`pnpm-lock.yaml` exists).
- Source root: `src/`.
- Path alias: `@/* -> ./src/*` (`tsconfig.json`).
- Formatter: Prettier + `prettier-plugin-tailwindcss`.
- Deploy scripts include OpenNext Cloudflare and Wrangler typegen.

## 2) Command Policy

Run commands from repo root:

`D:\PROJECT\Markdown\blog\2025-blog-public`

Use `pnpm` for scripts and package execution.

## 3) Scripts from package.json

### Install

```bash
pnpm i
```

### Develop

```bash
pnpm dev
# next dev --turbopack -p 2025
```

### Build / Start

```bash
pnpm build
pnpm start
```

### Cloudflare/OpenNext

```bash
pnpm build:cf
pnpm preview
pnpm deploy
pnpm cf-typegen
```

### Utility

```bash
pnpm svg
```

## 4) Lint / Test / Typecheck Reality

Current state:

- No `lint` script in `package.json`.
- No `test` script in `package.json`.
- No ESLint config (`eslint.config.*` / `.eslintrc*` not found).
- TypeScript is strict (`strict: true`), but `next.config.ts` sets:
  - `typescript.ignoreBuildErrors = true`

Implication: `pnpm build` can pass even when TS has errors.
Always run explicit `tsc --noEmit` after TS/TSX edits.

## 5) Verification Commands to Use

```bash
pnpm exec prettier . --check
pnpm exec prettier . --write
pnpm exec tsc --noEmit
pnpm build
```

No repository test framework is configured today.

## 6) Single-Test Commands (Future Templates)

If Vitest is introduced:

```bash
pnpm exec vitest run path/to/file.test.ts
pnpm exec vitest run path/to/file.test.ts -t "case name"
```

If Jest is introduced:

```bash
pnpm exec jest path/to/file.test.ts
pnpm exec jest path/to/file.test.ts -t "case name"
```

These are templates only; do not assume they work now.

## 7) Cursor / Copilot Rules Check

Checked locations:

- `.cursorrules`
- `.cursor/rules/`
- `.github/copilot-instructions.md`

Result: none found in current repository.

## 8) Formatting Rules (from .prettierrc)

- Tabs enabled (`useTabs: true`, `tabWidth: 2`).
- Single quotes in TS/TSX and JSX.
- No semicolons.
- No trailing commas.
- `printWidth: 160`.
- `arrowParens: avoid`.
- Tailwind class order is formatter-managed.

## 9) Imports and Module Patterns

- Prefer alias imports from `@/` for `src` modules.
  - Example: `import { cn } from '@/lib/utils'`
- Keep external imports separate from local imports.
- Use `import type` for type-only imports where suitable.
- Avoid unnecessary import reordering churn.

## 10) TypeScript Conventions

- Respect strict typing; avoid implicit `any`.
- Prefer specific types, unions, generics, or `unknown` + narrowing.
- Export stable public types for reusable module boundaries.
- Keep feature-local types close to usage (common `types.ts` pattern).

## 11) Naming Conventions (Observed)

- Components: PascalCase identifiers (often in kebab-case files).
  - Example: `Card` in `src/components/card.tsx`
- Functions/variables/hooks: camelCase.
- Hooks follow `useXxx` (`useSize`, `useAuth`).
- Zustand stores often use `useXxxStore`.

## 12) Error Handling Expectations

- Use `try/catch` for recoverable async flows.
- Throw contextual `Error` messages for failed remote operations.
- Do not silently swallow failures.
- For user flows, progress/error feedback often uses `sonner` toasts.

## 13) Architecture Layout (Observed)

- App Router pages/routes: `src/app`.
- Shared UI primitives/components: `src/components`.
- Cross-cutting logic/utilities: `src/lib`.
- Reusable hooks: `src/hooks`.
- Feature areas commonly organize into `components/`, `services/`, `stores/`, `types.ts`.

Favor existing boundaries instead of introducing new structure styles.

## 14) Agent Workflow in This Repo

When you modify code:

1. Match style and conventions used in the touched module.
2. Format and typecheck:
   - `pnpm exec prettier . --write`
   - `pnpm exec tsc --noEmit`
3. Build-check with `pnpm build`.
4. If adding lint/test tooling, update scripts and this file in same PR.

## 15) Security and Configuration Hygiene

- README highlights GitHub App private key sensitivity.
- Never commit secrets or key material (`.pem`, tokens, credentials).
- Prefer environment variables for deployment configuration.

## 16) Obsidian Vault Integration (obsidian-opencode plugin)

This repo integrates with an Obsidian vault for knowledge management. The plugin lives in `D:\PROJECT\Markdown\Obsidian\.obsidian\plugins/obsidian-opencode/`.

### Build Commands (Obsidian Plugin)

```bash
cd D:\PROJECT\Markdown\Obsidian\.obsidian\plugins\obsidian-opencode

bun install          # Install dependencies
bun run dev          # Development build (watch mode)
bun run build        # Production build (type-check + bundle)
bun test             # Run all tests
```

**Single test execution:**

```bash
bun test <pattern>   # Run tests matching pattern
bun test ProcessManager  # Run ProcessManager tests only
```

**Output:**

- `main.js` - CommonJS bundle for Obsidian
- Type-check runs via `tsc -noEmit -skipLibCheck`

### Plugin Code Style

| Type                | Convention                              | Example                                  |
| ------------------- | --------------------------------------- | ---------------------------------------- |
| Classes             | PascalCase                              | `OpenCodePlugin`, `ProcessManager`       |
| Interfaces/Types    | PascalCase                              | `OpenCodeSettings`, `ProcessState`       |
| Constants           | UPPER_CASE or camelCase                 | `DEFAULT_SETTINGS`, `OPENCODE_VIEW_TYPE` |
| Variables/functions | camelCase                               | `getVaultPath`, `startServer`            |
| Private members     | camelCase (no prefix)                   | `private processManager`                 |
| Files               | PascalCase (classes), lowercase (entry) | `ProcessManager.ts`, `main.ts`           |

### Plugin TypeScript Patterns

- Use union types for state: `"stopped" | "starting" | "running" | "error"`
- Use `async/await` over raw Promises
- Explicit return types on public methods
- Always handle null/undefined (strictNullChecks enabled)

### Obsidian API Patterns

- Extend `Plugin` with `onload()`/`onunload()` lifecycle
- Extend `ItemView` for views: `getViewType()`, `onOpen()`, `onClose()`
- Extend `PluginSettingTab` for settings: `display()`
- DOM helpers: `createEl()`, `createDiv()`, `setIcon()`

### Plugin Project Structure

```
.obsidian/plugins/obsidian-opencode/
├── src/
│   ├── main.ts           # Plugin entry, extends Plugin
│   ├── types.ts          # Types and constants
│   ├── OpenCodeView.ts   # Sidebar view (ItemView) with iframe
│   ├── ProcessManager.ts # Server process lifecycle
│   ├── SettingsTab.ts    # Settings UI (PluginSettingTab)
│   └── icons.ts          # Icon registration
├── tests/
│   └── ProcessManager.test.ts
├── esbuild.config.mjs
├── tsconfig.json
└── package.json
```

### Desktop-Only Features

The plugin uses Node.js APIs unavailable on mobile:

- `child_process.spawn()` for server process
- File system via vault adapter

Check for desktop environment before adding mobile-incompatible features.

### Testing in Obsidian Plugin

- Use Bun test framework: `import { describe, test, expect } from "bun:test"`
- Test file location: `tests/*.test.ts`
- Use `beforeAll` to verify test prerequisites
- Use `afterEach` for cleanup

```typescript
afterEach(async () => {
	if (currentManager) {
		currentManager.stop()
		await new Promise(resolve => setTimeout(resolve, 500))
		currentManager = null
	}
})
```

---

If tooling changes (tests, lint, CI, formatting), update `AGENTS.md` immediately.
