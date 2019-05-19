package com.myproject.myapplication

import android.app.DatePickerDialog
import android.app.Dialog
import android.os.Bundle
import android.support.v4.app.DialogFragment
import java.util.*


class DatePickerDialogFragment : DialogFragment() {

    override fun onCreateDialog(savedInstanceState: Bundle?): Dialog {
        val date = arguments?.getSerializable("date") as Date?
        val c = GregorianCalendar.getInstance()
        if (date != null) {
            c.time = date
        }
        val year = c.get(Calendar.YEAR)
        val month = c.get(Calendar.MONDAY)
        val day = c.get(Calendar.DAY_OF_MONTH)

        return DatePickerDialog(context!!, activity as TodoEditingActivity, year, month, day)
    }

}
