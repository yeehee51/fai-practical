## Git & GitHub Getting Started

### Prerequisites
1. Install Git: `git --version` (if not installed, download from git-scm.com)
2. Create GitHub account

### Setup (One-time)
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Getting Started Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/cklee-test/fai-practical.git
   cd fai-practical
   ```

2. **Create your branch**
   ```bash
   git checkout -b yourname
   ```

3. **Make changes**
   - Edit files or add new ones
   - Save your work

4. **Check status**
   ```bash
   git status
   ```

5. **Add and commit**
   ```bash
   git add .
   git commit -m "Add: describe your changes"
   ```

6. **Push to GitHub**
   ```bash
   git push origin student-yourname
   ```

7. **Create Pull Request**
   - Go to GitHub repository
   - Click "Compare & pull request"
   - Add description and submit

### Daily Workflow
```bash
git pull origin main    # Get latest changes
# Make your edits
git add .
git commit -m "Your message"
git push origin student-yourname
```
