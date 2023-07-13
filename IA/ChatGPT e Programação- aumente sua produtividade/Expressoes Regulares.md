# Expressões regulares

Suponha que o governo determine uma mudança no formato do número do CRM dos médicos, que a partir de agora deve seguir o seguinte padrão: ```XXXXXX-XX/UF.```

Na classe DadosCadastroMedico o atributo crm está anotado com:

```
@Pattern(regexp = "\\d{4,6}")
```

Utilize o ChatGPT para te auxiliar na mudança dessa regex para o novo padrão citado anteriormente.
