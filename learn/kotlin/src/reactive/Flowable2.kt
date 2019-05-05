package reactive

import io.reactivex.Flowable
import io.reactivex.schedulers.Schedulers
import kotlinx.coroutines.delay
import kotlinx.coroutines.runBlocking
import org.reactivestreams.Subscriber
import org.reactivestreams.Subscription

fun main(args: Array<String>) {
    Flowable.range(1, 15).map { MyItem1(it) }.observeOn(Schedulers.io())
            .subscribe(object : Subscriber<MyItem1> {
                lateinit var subscription: Subscription

                override fun onComplete() {
                    println("Done!")
                }

                override fun onSubscribe(s: Subscription) {
                    this.subscription = s
                    subscription.request(5)

                }

                override fun onNext(t: MyItem1?) {
                    runBlocking { delay(50) }
                    println("Subscriber received ${t!!}")
                    if (t.id == 5) {
                        println("Requesting two more")
                        subscription.request(2)
                    }
                }

                override fun onError(t: Throwable) {
                    t.printStackTrace()
                }
            })

    runBlocking { delay(10000) }
}

data class MyItem1(val id: Int) {
    init {
        println("MyItem Created $id")
    }
}
