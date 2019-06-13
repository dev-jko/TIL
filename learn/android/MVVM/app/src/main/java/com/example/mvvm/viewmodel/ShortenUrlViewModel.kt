package com.example.mvvm.viewmodel

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import android.util.Patterns
import com.example.mvvm.model.Repository
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.schedulers.Schedulers

class ShortenUrlViewModel(private val repository: Repository) : DisposableViewModel() {

    private val _shortenUrl = MutableLiveData<String>()
    private val _error = MutableLiveData<String>()
    private val _clickCopyToClipboard = SingleLiveEvent<String>()
    private val _clickOpenWeb = SingleLiveEvent<String>()
    private val _clickConvert = SingleLiveEvent<Any>()

    val showResult = MutableLiveData<Boolean>()

    val shortenUrl: LiveData<String> get() = _shortenUrl
    val error: LiveData<String> get() = _error
    val clickCopyToClipboard: LiveData<String> get() = _clickCopyToClipboard
    val clickOpenWeb: LiveData<String> get() = _clickOpenWeb
    val clickConvert: LiveData<Any> get() = _clickConvert

    fun getUrlValidator(errorMessage: String): METValidator {
        return RegexpValidator(errorMessage, Patterns.WEB_URL.pattern())
    }

    fun getShortenUrl(url: String) {
        repository.getShortenUrl(url)
            .subscribeOn(Schedulers.io())
            .observeOn(AndroidSchedulers.mainThread())
            .subscribe(
                {
                    showResult.postValue(true)
                    _shortenUrl.postValue(it.url)
                },
                {
                    _error.postValue(it.message)
                }
            )
            .apply { addDisposable(this) }
    }

    fun clickConvert() {
        _clickConvert.call()
    }

    fun clickCopyToClipboard() {
        _clickCopyToClipboard.value = _shortenUrl.value
    }

    fun clickOpenWeb() {
        _clickOpenWeb.value = _shortenUrl.value
    }


}