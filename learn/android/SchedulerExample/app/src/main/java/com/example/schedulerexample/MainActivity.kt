package com.example.schedulerexample

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import io.reactivex.Observable
import io.reactivex.disposables.CompositeDisposable
import io.reactivex.rxkotlin.addTo
import java.util.concurrent.TimeUnit
import javax.inject.Inject

class MainActivity : AppCompatActivity() {

    @Inject
    lateinit var schedulers: MySchedulers

    private val compositeDisposable = CompositeDisposable()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        (application as MyApplication).getComponent().inject(this)

        Observable.interval(500, TimeUnit.MILLISECONDS, this.schedulers.computation())
            .doOnNext { println("observable1 : computation - ${Thread.currentThread().name}") }
            .observeOn(schedulers.ui())
            .subscribe { println("observable1 : ui - ${Thread.currentThread().name}") }
            .addTo(compositeDisposable)


        Observable.interval(600, TimeUnit.MILLISECONDS, this.schedulers.computation())
            .doOnNext { println("observable1 : computation - ${Thread.currentThread().name}") }
            .observeOn(schedulers.ui())
            .subscribe { println("observable2 : ui - ${Thread.currentThread().name}") }
            .addTo(compositeDisposable)


    }

    override fun onDestroy() {
        super.onDestroy()
        this.compositeDisposable.clear()
    }
}
