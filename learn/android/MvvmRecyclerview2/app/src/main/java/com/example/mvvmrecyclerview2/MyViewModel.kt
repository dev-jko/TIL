package com.example.mvvmrecyclerview2

import android.app.Application
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.LiveData
import androidx.lifecycle.MediatorLiveData
import androidx.lifecycle.MutableLiveData

class MyViewModel(application: Application) : AndroidViewModel(application) {

    private val observableMyData: MediatorLiveData<List<MyData>> = MediatorLiveData()

    init {
//        observableMyData.addSource((application as BasicApp).getDataList(), observableMyData::postValue)
        observableMyData.addSource(getDataList(), observableMyData::postValue)
    }

    fun getMyData(): LiveData<List<MyData>> {
        return observableMyData
    }



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
