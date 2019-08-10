package com.nadarm.recyclerviewposition

import androidx.lifecycle.ViewModel
import io.reactivex.Observable
import io.reactivex.rxkotlin.withLatestFrom
import io.reactivex.subjects.BehaviorSubject
import java.util.concurrent.TimeUnit

class myViewModel : ViewModel() {

    val subject: BehaviorSubject<List<String>> = BehaviorSubject.create()


    init {

        Observable.interval(5000, TimeUnit.MILLISECONDS)
            .withLatestFrom(Observable.just(this.makeList())) { _, list ->
                list
            }
            .subscribe(subject)

    }


    private fun makeList(): List<String> {
        return (1..50).map { it.toString() }
    }

}