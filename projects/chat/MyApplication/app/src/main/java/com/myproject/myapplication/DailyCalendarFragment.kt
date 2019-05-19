package com.myproject.myapplication

import android.os.Bundle
import android.support.v4.app.Fragment
import android.support.v7.widget.DividerItemDecoration
import android.support.v7.widget.LinearLayoutManager
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.RelativeLayout
import com.myproject.myapplication.myrecyclerview.DailyAdapter
import io.reactivex.Observable
import kotlinx.android.synthetic.main.fragment_daily_calendar.*
import java.sql.Date
import java.util.*

import kotlin.collections.ArrayList


class DailyCalendarFragment : Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        return inflater.inflate(R.layout.fragment_daily_calendar, container, false) as RelativeLayout
    }

    override fun onActivityCreated(savedInstanceState: Bundle?) {
        super.onActivityCreated(savedInstanceState)

        val todoList: List<CalendarData> = getData()
        val gregorianCalendar = GregorianCalendar()
        gregorianCalendar.add(Calendar.DATE, -10)
        val dayList: List<Date> = Observable.range(0, 50)
            .map {
                gregorianCalendar.add(Calendar.DATE, 1)
                Date(gregorianCalendar.time.time)
            }
            .toList().blockingGet()

        recycler_daily.addItemDecoration(DividerItemDecoration(context, DividerItemDecoration.VERTICAL))
        recycler_daily.layoutManager = LinearLayoutManager(activity)
        val adapter = DailyAdapter(dayList, todoList)
        recycler_daily.adapter = adapter
    }

    fun getData(): List<CalendarData> {
        val arrayList = ArrayList<CalendarData>()
        val db = (activity as MainActivity).dbHelper.readableDatabase


//        val db2 = (activity as MainActivity).dbHelper.writableDatabase
//        for (i in 1..20) {
//            val gregorianCalendar = GregorianCalendar()
//            val start = gregorianCalendar.time.time.toString()
//            gregorianCalendar.add(Calendar.DATE, i)
//            val end = gregorianCalendar.time.time.toString()
//            val content = "할일$i"
//            val query1 = "INSERT INTO calendar (START_DATE, END_DATE, CONTENT) " +
//                    "VALUES($start, $end, '$content')"
//            Log.d("/*-/*-/*-/*-", query1)
//            db2.execSQL(query1)
//        }


        val query = "SELECT * FROM calendar"
        val cursor = db.rawQuery(query, null)
        while (cursor.moveToNext()) {
            val temp = CalendarData(
                cursor.getInt(0),
                Date(cursor.getLong(1)),
                Date(cursor.getLong(2)),
                cursor.getString(3)
            )
            arrayList.add(temp)
        }
        return arrayList.toList()
    }

}
