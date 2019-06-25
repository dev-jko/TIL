package com.example.dogapiretrofit.viewmodel

import android.util.Log
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.dogapiretrofit.api.DogRetrofit
import com.example.dogapiretrofit.ui.DogAdapter
import io.reactivex.Observable
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.disposables.CompositeDisposable
import io.reactivex.rxkotlin.mergeAll
import io.reactivex.schedulers.Schedulers

class DogViewModel : ViewModel() {

    val liveDataimgUrlList: MutableLiveData<List<String>> = MutableLiveData()
    private val compositeDisposable = CompositeDisposable()

    init {
        liveDataimgUrlList.postValue(listOf(""))
    }

    fun getNewDogImgUrls(adapter: DogAdapter) {
        Observable.range(0, 10)
            .map { DogRetrofit.getInstance().getDogImgUrlObservable() }
            .mergeAll()
            .subscribeOn(Schedulers.io())
            .subscribeOn(AndroidSchedulers.mainThread())
            .doOnSubscribe {
                adapter.dogImgUrlList.clear()
                adapter.notifyDataSetChanged()
            }
            .observeOn(AndroidSchedulers.mainThread())
            .subscribe(
                { adapter.addDogImgUrl(it) },
                { Log.e("Err", "retrofit subscribe error : ${it.printStackTrace()}") },
                { Log.d("DogViewModel", "completed") }
            ).apply { compositeDisposable.add(this) }
    }

    fun appendDogItem(adapter: DogAdapter) {
        DogRetrofit.getInstance().getDogImgUrlObservable()
            .subscribeOn(Schedulers.io())
            .observeOn(AndroidSchedulers.mainThread())
            .subscribe(
                { adapter.addDogImgUrl(it) },
                { Log.e("Err", "retrofit subscribe error : ${it.printStackTrace()}") },
                { Log.d("DogViewModel", "completed") }
            ).apply { compositeDisposable.add(this) }
    }

}