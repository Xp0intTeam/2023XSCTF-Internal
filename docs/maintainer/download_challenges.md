This document shows how to download all challenges on `2021JNUCTF-internal` repository.

1. Setup credential (Ask @xf1les for `SECRET_TOKEN`):  
```
$ echo "https://xf1les:<SECRET_TOKEN>@github.com" > ~/.git-credentials
$ git config --global credential.helper store
```

2. Clone `2021JNUCTF-internal` and fetch all challenges with `git submodule update` command:
```
$ git clone https://github.com/xf1les/2021JNUCTF-internal && cd 2021JNUCTF-internal
$ git submodule update --init --remote
```

3. Now all challenges should have download in the `challenge-type` directories.
```
$ ls -ld PWN/*/ Reverse/*/ WEB/*/ Crypto/*/ MISC/*/
```

4. Run this command to sync challenges from remote repositories:
```
$ git submodule update --remote
```
