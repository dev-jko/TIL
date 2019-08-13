package com.example.schedulerexample

import dagger.Component
import io.reactivex.Scheduler
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.schedulers.Schedulers
import javax.inject.Inject
import javax.inject.Singleton


@Singleton
@Component
interface MyComponent {

    fun inject(activity: MainActivity)

}


@Singleton
class MySchedulers @Inject constructor() {
    fun ui(): Scheduler = AndroidSchedulers.mainThread()
    fun io(): Scheduler = Schedulers.io()
    fun computation(): Scheduler = Schedulers.computation()
}