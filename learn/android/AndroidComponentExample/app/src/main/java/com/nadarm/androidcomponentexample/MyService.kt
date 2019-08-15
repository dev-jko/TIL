package com.nadarm.androidcomponentexample

import android.app.Service
import android.content.Intent
import android.os.IBinder
import io.reactivex.Observable
import io.reactivex.disposables.CompositeDisposable
import io.reactivex.rxkotlin.addTo
import java.util.concurrent.TimeUnit

class MyService : Service() {

    companion object {
        var count = 0
    }

    private val myCount = count++
    private val compositeDisposable = CompositeDisposable()

    override fun onCreate() {
        super.onCreate()
        println("MyService - $myCount, on create, ${Thread.currentThread().name}")
    }

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        println("MyService - $myCount, on start command, ${Thread.currentThread().name}")

        Observable.interval(500, TimeUnit.MILLISECONDS)
            .take(10)
            .subscribe(
                { println("MyService - $myCount, Observable interval $it, ${Thread.currentThread().name}") },
                {},
                { stopSelf() }
            )
            .addTo(compositeDisposable)

        return super.onStartCommand(intent, flags, startId)
    }

    override fun onBind(intent: Intent?): IBinder? {
        println("MyService - $myCount, on bind, ${Thread.currentThread().name}")
        return null
    }

    override fun onUnbind(intent: Intent?): Boolean {
        println("MyService - $myCount, on unbind, ${Thread.currentThread().name}")
        return super.onUnbind(intent)
    }

    override fun onDestroy() {
        super.onDestroy()
        compositeDisposable.clear()
        println("MyService - $myCount, on destroy, ${Thread.currentThread().name}")
    }
}
