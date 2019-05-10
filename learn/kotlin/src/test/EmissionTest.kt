package test

import io.reactivex.Observable
import io.reactivex.schedulers.Schedulers
import org.junit.Test
import java.util.concurrent.atomic.AtomicInteger
import kotlin.test.assertEquals


class EmissionTest {

    @Test
    fun `check emissions count`() {
        val emissionsCount = AtomicInteger()
        Observable.range(1, 10)
                .subscribeOn(Schedulers.computation())
                .blockingSubscribe { emissionsCount.incrementAndGet() }
        assertEquals(10, emissionsCount.get())
    }
}