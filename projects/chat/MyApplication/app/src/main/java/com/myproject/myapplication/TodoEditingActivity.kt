package com.myproject.myapplication

import android.app.DatePickerDialog
import android.os.Bundle
import android.support.v7.app.AppCompatActivity
import android.widget.DatePicker
import kotlinx.android.synthetic.main.activity_todo_editing.*
import java.util.*

class TodoEditingActivity : AppCompatActivity(), DatePickerDialog.OnDateSetListener {

    lateinit var startDate: Date
    lateinit var endDate: Date
    var datePickerFlag = 0

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_todo_editing)

        startDate = intent.getSerializableExtra("startDate") as Date
        endDate = intent.getSerializableExtra("endDate") as Date

        text_view_todo_editing_start_date.text = startDate.toString()
        text_view_todo_editing_end_date.text = endDate.toString()


        linear_layout_todo_editing_start.setOnClickListener {
            val dialog = DatePickerDialogFragment()
            val bundle = Bundle()
            bundle.putSerializable("date", startDate)
            dialog.arguments = bundle
            datePickerFlag = 0
            dialog.show(this.supportFragmentManager, "startDatePicker")
        }

        linear_layout_todo_editing_end.setOnClickListener {
            val dialog = DatePickerDialogFragment()
            val bundle = Bundle()
            bundle.putSerializable("date", endDate)
            dialog.arguments = bundle
            datePickerFlag = 1
            dialog.show(this.supportFragmentManager, "endDatePicker")
        }


        // TODO 취소 버튼, 저장 버튼 구현

    }

    override fun onDateSet(view: DatePicker?, year: Int, month: Int, dayOfMonth: Int) {
        val c = GregorianCalendar.getInstance()
        c.set(year, month, dayOfMonth)
        if (datePickerFlag == 0) {
            startDate.time = c.timeInMillis
            text_view_todo_editing_start_date.text = startDate.toString()
        } else {
            endDate.time = c.timeInMillis
            text_view_todo_editing_end_date.text = endDate.toString()
        }
    }


}
