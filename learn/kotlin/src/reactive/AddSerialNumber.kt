package reactive

import io.reactivex.Observable
import io.reactivex.ObservableOperator
import io.reactivex.Observer
import io.reactivex.disposables.Disposable
import io.reactivex.rxkotlin.subscribeBy
import java.util.concurrent.atomic.AtomicInteger

class AddSerialNumber<T> : ObservableOperator<Pair<Int, T>, T> {
    val counter: AtomicInteger = AtomicInteger()

    override fun apply(observer: Observer<in Pair<Int, T>>): Observer<in T> {
        return object : Observer<T> {
            override fun onComplete() {
                observer.onComplete()
            }

            override fun onSubscribe(d: Disposable) {
                observer.onSubscribe(d)
            }

            override fun onNext(t: T) {
                observer.onNext(Pair(counter.incrementAndGet(), t))
            }

            override fun onError(e: Throwable) {
                observer.onError(e)
            }
        }
    }
}

fun main(args: Array<String>) {
    Observable.range(50, 20)
            .lift(AddSerialNumber<Int>())
            .subscribeBy(
                    onNext = { println("Next $it") },
                    onError = { it.printStackTrace() },
                    onComplete = { println("Completed") }
            )
}