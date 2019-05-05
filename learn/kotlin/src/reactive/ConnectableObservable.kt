package reactive

import io.reactivex.Observable
import io.reactivex.rxkotlin.toObservable
import kotlinx.coroutines.delay
import kotlinx.coroutines.runBlocking
import java.util.concurrent.TimeUnit

fun main(args: Array<String>) {
    val connectableObservable = listOf("String1", "String2", "String3").toObservable().publish()
    connectableObservable.subscribe { println("Subscription 1: $it") }
    connectableObservable.map(String::reversed).subscribe { println("Subscription 2: $it") }
    connectableObservable.connect()
    connectableObservable.subscribe { println("Subscription 3: $it") }

    val connectableObservable2 = Observable.interval(100, TimeUnit.MILLISECONDS).publish()
    connectableObservable2.subscribe { println("Subscription 1: $it") }
    connectableObservable2.subscribe { println("Subscription 2: $it") }
    connectableObservable2.connect()
    runBlocking { delay(300) }
    connectableObservable2.subscribe { println("Subscription 3: $it") }
    runBlocking { delay(300) }
}