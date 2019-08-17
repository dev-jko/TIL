package com.nadarm.androidcomponentexample

import android.app.IntentService
import android.content.Intent
import android.os.IBinder
import io.reactivex.Observable
import io.reactivex.disposables.CompositeDisposable
import io.reactivex.rxkotlin.addTo
import io.reactivex.rxkotlin.toObservable
import java.util.concurrent.TimeUnit

class MyIntentService : IntentService(MyIntentService::class.java.simpleName) {

    companion object {
        var count = 0
    }

    private val myCount = count++
    private val compositeDisposable = CompositeDisposable()


    override fun onCreate() {
        super.onCreate()
        println("My Intent Service - $myCount, on create, ${Thread.currentThread().name}")
    }

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        println("My Intent Service - $myCount, on start command, ${Thread.currentThread().name}")
        return super.onStartCommand(intent, flags, startId)
    }

    override fun onBind(intent: Intent?): IBinder? {
        println("My Intent Service - $myCount, on bind, ${Thread.currentThread().name}")
        return super.onBind(intent)
    }

    override fun onHandleIntent(intent: Intent?) {
        println("My Intent Service - $myCount, on handle intent, ${Thread.currentThread().name}")

        Observable.interval(0, 500, TimeUnit.MILLISECONDS)
            .take(10)
            .subscribe(
                { println("My Intent Service - $myCount, interval on next $it, ${Thread.currentThread().name}") },
                { println("My Intent Service - $myCount, interval on error, ${Thread.currentThread().name}") },
                { println("My Intent Service - $myCount, interval on complete, ${Thread.currentThread().name}") }
            )
            .addTo(compositeDisposable)

        (1..5).toObservable()
            .subscribe(
                { println("My Intent Service - $myCount, iterable on next $it, ${Thread.currentThread().name}") },
                { println("My Intent Service - $myCount, iterable on error, ${Thread.currentThread().name}") },
                { println("My Intent Service - $myCount, iterable on complete, ${Thread.currentThread().name}") }
            )
            .addTo(compositeDisposable)

    }

    override fun onDestroy() {
        super.onDestroy()
//        compositeDisposable.clear()
        println("My Intent Service - $myCount, on destroy, ${Thread.currentThread().name}")
    }
}