package com.example.mvvmrecyclerview

fun getLanguageCodeList(): List<LanguageCode>? {
    return listOf(
        LanguageCode("헝가리어", "hu"),
        LanguageCode("한국어", "ko"),
        LanguageCode("이탈리아어", "it"),
        LanguageCode("포르투갈어", "pt"),
        LanguageCode("태국어", "th")
    )
}