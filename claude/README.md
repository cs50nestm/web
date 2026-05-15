# Installing Claude Code
## Step-by-step setup guide for macOS

> **Note:** You do not need a Claude subscription to install — the subscription is only required when you log in for the first time.

---

## Installation Steps

**Step 1 — Open the Terminal**
Press `Cmd + Space`, type `Terminal`, and press Enter.

**Step 2 — Run the installer**
Copy and paste:

```bash
curl -fsSL https://claude.ai/install.sh | sh
```

Then hit `enter`.

The installer downloads Claude Code, places it in the right location, and sets up your PATH automatically. It takes under a minute.

**Step 3 — Open a new terminal window**
Close your current terminal and open a fresh one. This ensures your shell picks up the new PATH entry.

**Step 4 — Verify the installation**

```bash
claude --version
```

You should see a version number. If you see `command not found`, make sure you opened a new terminal window after installing.

**Step 5 — Log in to your Claude account**

```bash
claude
```

A browser window will open asking you to sign in. You need a Claude Pro subscription ($20/month) to proceed. Follow the prompts — once authenticated you are ready to go.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `command not found` after install | Close the terminal completely, open a new window, try again |
| Browser doesn't open on login | Try running: `claude auth login` |
| Installer stalls or errors | Check your internet connection, then run the curl command again |

---

## What's Next

Navigate to your project folder and run `claude` to start a session:
mkdir my-app
cd my-app
claude

Claude Code will scan your directory and give you a prompt. Direct it in plain English from there.
