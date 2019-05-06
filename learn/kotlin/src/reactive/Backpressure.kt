package reactive

import io.reactivex.BackpressureStrategy
import io.reactivex.Flowable
import io.reactivex.schedulers.Schedulers
import kotlinx.coroutines.delay
import kotlinx.coroutines.runBlocking
import org.reactivestreams.Subscriber
import org.reactivestreams.Subscription

fun main(args: Array<String>) {
    val subscriber = object : Subscriber<Int> {
        override fun onComplete() {
            println("All Completed")
        }

        override fun onSubscribe(s: Subscription) {
            println("New Subscription $s")
            s.request(10)
        }

        override fun onNext(t: Int?) {
            println("Next : $t")
        }

        override fun onError(t: Throwable) {
            t.printStackTrace()
        }
    }

    val flowable = Flowable.create<Int>({
        for (i in 1..10) {
            it.onNext(i)
        }
        it.onComplete()
    }, BackpressureStrategy.BUFFER)

    flowable.observeOn(Schedulers.io()).subscribe(subscriber)

    runBlocking { delay(10000) }
}