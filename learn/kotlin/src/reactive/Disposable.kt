import io.reactivex.Observable
import io.reactivex.Observer
import io.reactivex.disposables.Disposable
import kotlinx.coroutines.delay
import kotlinx.coroutines.runBlocking
import java.util.concurrent.TimeUnit

fun main(args: Array<String>) {
    runBlocking {
        val observable = Observable.interval(100, TimeUnit.MILLISECONDS)

        val observer = object : Observer<Long> {
            lateinit var disposable: Disposable

            override fun onComplete() {
                println("Completed")
            }

            override fun onSubscribe(d: Disposable) {
                disposable = d
            }

            override fun onNext(t: Long) {
                println("Next : $t")
                if(t >= 10 && !disposable.isDisposed){
                    disposable.dispose()
                    println("Disposed")
                }
            }

            override fun onError(e: Throwable) {
                println("Error : ${e.message}")
            }
        }

        observable.subscribe(observer)
        delay(1500)
    }
}