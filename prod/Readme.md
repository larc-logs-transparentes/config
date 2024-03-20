# Subir imagem Docker para registry do GitHub

## Login

Antes de subir alguma imagem, primeiramente é necessário realizar login na plataforma.

Para tal, é necessário que o usuário possua um token de acesso, com a permissão ```write_package```.

Esse token pode ser gerado por meio deste tutorial: [Creating a personal access token (classic)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic).

Realização do login:

```bash
export GITHUB_TOKEN="<COLOQUE AQUI O SEU TOKEN>"
echo $GITHUB_TOKEN | docker login ghcr.io -u USERNAME --password-stdin
``` 

