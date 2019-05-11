package test

import io.reactivex.Observable
import io.reactivex.observers.TestObserver
import io.reactivex.schedulers.TestScheduler
import org.junit.Test
import java.util.concurrent.TimeUnit

class SchedulerTest {
    @Test
    fun `test by fast forwarding time`() {
        val testScheduler = TestScheduler()
        val observable = Observable.interval(5, TimeUnit.MINUTES, testScheduler)
        val testObserver = TestObserver<Long>()

        observable.subscribe(testObserver)

        testObserver.assertSubscribed()
        testObserver.assertValueCount(0)

        testScheduler.advanceTimeBy(100, TimeUnit.MINUTES)
        testObserver.assertValueCount(20)

        testScheduler.advanceTimeBy(400, TimeUnit.MINUTES)
        testObserver.assertValueCount(100)
    }
}