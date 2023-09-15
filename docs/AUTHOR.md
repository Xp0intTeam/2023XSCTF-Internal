This document shows how to build and submit a CTF challenge to `2022XSCTF-internal` repository.

# 🔨 Build a challenge

A challenge should consist of three parts:

1. **`build/`**: a directory where stores files used to build the challenge. It is only required in PWN and WEB, and optional in other types of challenges.

2. **`player/`**: a directory where stores files to be distributed to players (which is usually a `zip` or `tar.gz` file).

3. **`README.md`**: a Markdown document containing basic information about the challenge (name, type, difficulty, flag, writeup and so on).

Before building, you should create a Github repository to store challenge files with the following steps:
1. Create a repository on [*Xp0intTeam*](https://github.com/Xp0intTeam) organization named in `2022XSCTF_<the name of your challenge>` form.
2. Goto `Settings -> Collaborators and teams`，add teams `JNUCTF-Authors-2022`.
3. Copy `build/`, `player/` and `README.md` in `2022XSCTF-internal/<challenge-type>/sample/` to the root directory of the repository.
4. Make sure all files are on **main** branch (not master branch).
5. Finally, you can start your building now ⚡.

# 📩 Submit challenge to `2022XSCTF-internal` repository

After creating the challenge repository, you should submit it to `2022XSCTF-internal` repository to let others learn about your challenge and know the progress of its development.

The basic idea is using `submodule` feature from Git. With `submodule`, maintainers (with  a secret token issued from [Xp0intTeam](https://github.com/Xp0intTeam)) can download all challenges submited on `2022XSCTF-internal` repository with a single command when deploying them on remote server.

Please note that **`2022XSCTF-internal` repository won't store any files from challenge repositories,** it just stores a metadata referencing to the repositories.

Assume that you have a PWN challenge `my_pwn_chall` which is stored at `https://github.com/myusername/2022XSCTF_my_pwn_chall`, follow these steps to submit you challenge:

1. Clone `2022XSCTF-internal` repository from Github:  
```
$ git clone https://github.com/Xp0intTeam/2022XSCTF-internal && cd 2022XSCTF-internal/
```
2. Create a submodule linked to the repository in `PWN/` directory:
```
$ git submodule add https://github.com/myusername/2022XSCTF_my_pwn_chall PWN/my_pwn_chall
```
3. Edit `CHALLENGES.md` or ``CHALLENGES_Final.md`` in the root directory, add information about your challenge.  

4. Finally, commit and push to Github:  
```
$ git add -A && git commit -m "Add Pwn challenge my_pwn_chall"
$ git push
```

# 🌍 Publish challenge to `2022XSCTF` repository

Unlike `2022XSCTF-internal`, `2022XSCTF` **stores files from your challenge repositories** (specifically, `build/`, `player/` and `README.md`), not just the metadata.

`2022XSCTF` will be make public when official Writeup are published. **To publish challenge, you should create a pull request** instead of directly pushing to it.


**🚧 More information for this section is still working in progress 🚧**
