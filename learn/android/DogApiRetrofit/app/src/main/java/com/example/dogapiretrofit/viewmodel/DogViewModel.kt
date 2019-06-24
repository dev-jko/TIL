package com.example.dogapiretrofit.viewmodel

import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.dogapiretrofit.api.DogRetrofit

class DogViewModel : ViewModel() {

    val text: MutableLiveData<String> = MutableLiveData()


    fun getObservable() {
        DogRetrofit.getInstance().getDogImgUrlObservable()
            .subscribe {
                text.postValue(it.toString())
            }
    }

    fun appendDogItem(){
        getObservable()
    }

}