import io.reactivex.Observable
import io.reactivex.Observer
import io.reactivex.disposables.Disposable
import kotlinx.coroutines.delay
import kotlinx.coroutines.runBlocking
import java.util.concurrent.TimeUnit

fun main(args: Array<String>) {
    val observer: Observer<Any> = object : Observer<Any> {
        override fun onComplete() {
            println("Completed")
        }

        override fun onSubscribe(d: Disposable) {
            println("New Subscription, $d")
        }

        override fun onNext(t: Any) {
            println("Next Item : $t")
        }

        override fun onError(e: Throwable) {
            println("Error : ${e.message}")
        }
    }

    Observable.range(1, 10).subscribe(observer)
    Observable.empty<String>().subscribe(observer)
    runBlocking {
        Observable.interval(300, TimeUnit.MILLISECONDS).subscribe(observer)
        delay(900)
        Observable.timer(400, TimeUnit.MILLISECONDS).subscribe(observer)
        delay(400)
        delay(5000)
    }

}