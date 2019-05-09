package reactive

import io.reactivex.Observable
import io.reactivex.Observer
import io.reactivex.disposables.Disposable

fun main(args: Array<String>) {
    Observable.range(1, 20)
            .skipWhile { it < 10 }
            .subscribe(object : Observer<Int> {
                override fun onComplete() {
                    println("Completed")
                }

                override fun onSubscribe(d: Disposable) {
                    println("starting skipWhile")
                }

                override fun onNext(t: Int) {
                    println("Received $t")
                }

                override fun onError(e: Throwable) {
                    e.printStackTrace()
                }
            })
}