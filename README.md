# Akashic-Records

## 👨‍💻 Trabalho 2 de INF1407 - Programação para a Web
Integrantes do Grupo:

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/pvliborio">
        <img src="https://avatars.githubusercontent.com/u/19355448?v=4" width="100px;" alt="Foto do Paulo Vitor Libório "/><br>
        <sub>
          <b>Paulo Vítor Libório</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href= "https://github.com/LeeTgk">
        <img src="https://avatars.githubusercontent.com/u/61758137?v=4" width="100px;" alt="Foto de Kevin Abreu"/><br>
        <sub>
          <b>Kevin Abreu</b>
        </sub>
      </a>
    </td>
  </tr>
</table>


## ☕ Tema
A ideia do Trabalho é criar um site que dê acesso a alguns modelos de geração de texto gpt2, e permita que usuários salvem suas respostas, gerações favoritas em um perfil que pode ser acessado/editado através de um sistema de Login.

## 🚀 Usando Akashic Records

Akashic Records está atualmente sendo hosteado em: https://akashicrecords.herokuapp.com/
OBS: Por usarmos um plano free, não temos dynos(heroku app containers) dedicados o que significa que se não há acessos em um período de trinta minutos todos os dynos alocados entram em sleep e a aplicação só será recarregada quando o tráfego voltar.
Dito isso, tenha paciência e dê refresh algumas vezes se a página não carregar direito, o mesmo pode ser dito sobre os primeiros requests da API pois carregar o modelo pode demorar demais, com a solução também sendo refresh + computar novamente.

No site as operações possíveis são:
  * Login convencional:
  ![image](https://user-images.githubusercontent.com/61758137/144293768-4e5a8777-bcab-4b75-8895-b96cd0a2ce3e.png)
  * Registro:
  ![image](https://user-images.githubusercontent.com/61758137/144294293-c3cfd087-27bf-4273-bb31-3116df346838.png)
  * Gerar um texto resultado da api gpt2:
  ![image](https://user-images.githubusercontent.com/61758137/144291234-8bb2d09b-8de0-44b3-acc7-a63d6412d29d.png)
  * salva-lo caso esteja logado:
  
  ![image](https://user-images.githubusercontent.com/61758137/144292573-bb78da5f-3457-41eb-b371-8aea1924571a.png)
  * visualizar os resultados salvos, excluir:
  ![image](https://user-images.githubusercontent.com/61758137/144293016-ace93fe6-7c19-4e4a-b492-94680147ec0d.png)
  * ou editar o título:
  ![image](https://user-images.githubusercontent.com/61758137/144293297-5df944d0-d1fe-4fda-ac20-a883f1eb281b.png)

* Observações sobre o Uso:
A ideia do Serviço é ser um passatempo curioso, a fim de ver resultados interessantes e, ou engraçados.
Dito isso, condenamos o uso do mesmo na geração de textos que podem ser interpretados como verdade.
Como o próprio autor do modelo cita :
  > The training data used for this model come from Portuguese Wikipedia. We know it contains a lot of unfiltered content from the internet, which is far from neutral. 

## 🤝 Nossos Agradecimentos a:
Pierre Guillou, por ter treinado e disponibilizado o modelo em : 
  * https://huggingface.co/pierreguillou/gpt2-small-portuguese
Hugging Face pelo desenvimento da API que permite obtermos os resultados do modelo :
  * https://api-inference.huggingface.co/docs/python/html/quicktour.html
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/piegu">
        <img src="https://avatars.githubusercontent.com/u/20000948?v=4" width="100px;" alt="Foto de Pierre Guillou"/><br>
        <sub>
          <b>Pierre Guillou</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href= "https://huggingface.co/">
        <img src="https://huggingface.co/front/assets/huggingface_logo-noborder.svg" width="100px;" alt="Logo da Hugging Face"/><br>
        <sub>
          <b>Hugging Face</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

