package com.example.mvvm

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.Transformations
import androidx.lifecycle.ViewModel

class ProfileViewModel : ViewModel() {

    private val _name = MutableLiveData<String>().apply { postValue("initial name") }
    private val _lastName = MutableLiveData<String>().apply { postValue("initial last name") }
    private val _likes = MutableLiveData<Int>().apply { postValue(1) }

    val name: LiveData<String> = _name
    val lastName: LiveData<String> = _lastName
    val likes: LiveData<Int> = _likes

    val popularity: LiveData<Popularity> = Transformations.map(_likes) {
        when {
            it > 9 -> Popularity.STAR
            it > 4 -> Popularity.POPULAR
            else -> Popularity.NORMAL
        }
    }

    fun onLike() {
        _likes.value = (_likes.value ?: 0) + 1
    }

    fun changeName(){
        val currentName = _name.value
        val currentLastName = _lastName.value
        _name.postValue(currentLastName)
        _lastName.postValue(currentName)
    }

}

enum class Popularity {
    NORMAL,
    POPULAR,
    STAR
}