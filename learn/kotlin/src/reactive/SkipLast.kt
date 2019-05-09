package reactive

import io.reactivex.Observable
import io.reactivex.Observer
import io.reactivex.disposables.Disposable

fun main(args: Array<String>) {
    Observable.range(1, 20)
            .skipLast(5)
            .subscribe(object : Observer<Int> {
                override fun onComplete() {
                    println("Complete")
                }

                override fun onSubscribe(d: Disposable) {
                    println("starting skipLast(count)")
                }

                override fun onNext(t: Int) {
                    println("Received $t")
                }

                override fun onError(e: Throwable) {
                    e.printStackTrace()
                }
            })
}