package com.myproject.myapplication

import android.os.Bundle
import android.support.v4.app.Fragment
import android.support.v7.widget.LinearLayoutManager
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.RelativeLayout
import com.myproject.myapplication.myrecyclerview.DailyAdapter
import io.reactivex.Observable
import kotlinx.android.synthetic.main.fragment_two.*


class TwoFragment : Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        return inflater.inflate(R.layout.fragment_two, container, false) as RelativeLayout
    }

    override fun onActivityCreated(savedInstanceState: Bundle?) {
        super.onActivityCreated(savedInstanceState)

//        val dayList: List<String> = Observable.range(1, 50).map { "5월 ${it}일" }.toList().blockingGet()
        val dayList: List<String> = getData()
        recycler_daily.layoutManager = LinearLayoutManager(activity)
        val adapter = DailyAdapter(dayList)
        recycler_daily.adapter = adapter
    }

    fun getData(): List<String> {
        val arrayList = ArrayList<String>()
        val db = (activity as MainActivity).dbHelper.readableDatabase

//
//        val db2 = (activity as MainActivity).dbHelper.writableDatabase
//        for (i in 1..20) {
//            val start = "2019-05-$i"
//            val end = "2019-05-${i + 30}"
//            val content = "할일$i"
//            val query1 = "INSERT INTO calendar (START_DATE, END_DATE, CONTENT) " +
//                    "VALUES('$start', '$end', '$content')"
//            db2.execSQL(query1)
//        }


        val query = "SELECT * FROM calendar"
        val cursor = db.rawQuery(query, null)
        while (cursor.moveToNext()) {
            var temp = ""
            temp += cursor.getString(0) + ", "
            temp += cursor.getString(1) + ", "
            temp += cursor.getString(2) + ", "
            temp += cursor.getString(3)
            arrayList.add(temp)
        }
        return arrayList.toList()
    }

}
