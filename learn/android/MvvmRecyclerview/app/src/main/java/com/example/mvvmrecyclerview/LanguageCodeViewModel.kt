package com.example.mvvmrecyclerview

import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel

class LanguageCodeViewModel: ViewModel() {

    val liveLanguageCodeList = MutableLiveData<List<LanguageCode>>()

    init {
        liveLanguageCodeList.postValue(getLanguageCodeList())
    }

}