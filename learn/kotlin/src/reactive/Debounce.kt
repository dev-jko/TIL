package reactive

import io.reactivex.Observable
import kotlinx.coroutines.delay
import kotlinx.coroutines.runBlocking
import java.util.concurrent.TimeUnit

fun main(args: Array<String>) {
    createObservable().debounce(200, TimeUnit.MILLISECONDS).subscribe {
        println(it)
    }
}

fun createObservable(): Observable<String> =
        Observable.create<String> {
            it.onNext("R")
            runBlocking { delay(100) }
            it.onNext("Re")
            it.onNext("Reac")
            runBlocking { delay(130) }
            it.onNext("Reactiv")
            runBlocking { delay(140) }
            it.onNext("Reactive")
            runBlocking { delay(200) }
            it.onNext("Reactive Progr")
            runBlocking { delay(100) }
            it.onNext("Reactive Programm")
            runBlocking { delay(190) }
            it.onNext("Reactive Programming")
            runBlocking { delay(250) }
            it.onComplete()
        }
