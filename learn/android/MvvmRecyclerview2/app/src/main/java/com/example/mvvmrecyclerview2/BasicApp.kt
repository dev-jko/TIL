package com.example.mvvmrecyclerview2

import android.app.Application
import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData

class BasicApp : Application() {

    fun getDataList(): LiveData<List<MyData>> {
        val liveData = MutableLiveData<List<MyData>>()
        val list = listOf<MyData>(
            MyData("kim", 20),
            MyData("kang", 22),
            MyData("ko", 23),
            MyData("go", 25),
            MyData("ha", 27),
            MyData("lee", 29),
            MyData("oo", 30),
            MyData("fewa", 10),
            MyData("chi", 15),
            MyData("bab", 35),
            MyData("qq", 14),
            MyData("aca", 50)
        )
        liveData.postValue(list)
        return liveData
    }

}
