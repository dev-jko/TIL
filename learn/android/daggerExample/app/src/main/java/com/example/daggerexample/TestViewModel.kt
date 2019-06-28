package com.example.daggerexample

import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel

class TestViewModel : ViewModel() {

    val testString: MutableLiveData<String> = MutableLiveData("init")

    var count = 0

    fun onClicked() {
        testString.postValue("changed${++count}")
    }

}