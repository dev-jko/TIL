package com.myproject.myapplication

import android.content.Context
import android.os.Bundle
import android.support.v4.app.Fragment
import android.support.v4.app.FragmentManager
import android.support.v4.app.FragmentStatePagerAdapter
import android.support.v7.app.AppCompatActivity
import android.view.View
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    lateinit var dbHelper: CalendarOpenHelper

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        dbHelper = CalendarOpenHelper(this)

        pager.adapter = MyPagerAdapter(supportFragmentManager)
        pager.currentItem = this.getSharedPreferences("settings", Context.MODE_PRIVATE).getInt("pagerItem", 0)

        val movePageListener: View.OnClickListener = View.OnClickListener {
            val tag: Int = it.tag as Int
            pager.currentItem = tag
        }

        btn_monthly_tab.setOnClickListener(movePageListener)
        btn_monthly_tab.tag = 0
        btn_daily_tab.setOnClickListener(movePageListener)
        btn_daily_tab.tag = 1
        btn_weekly_tab.setOnClickListener(movePageListener)
        btn_weekly_tab.tag = 2
    }

    override fun onPause() {
        super.onPause()

        this.getSharedPreferences("settings", Context.MODE_PRIVATE).edit()
            .putInt("pagerItem", pager.currentItem)
            .apply()
    }

    class MyPagerAdapter(fm: FragmentManager) : FragmentStatePagerAdapter(fm) {
        override fun getItem(p0: Int): Fragment {
            return when (p0) {
                0 -> OneFragment()
                1 -> TwoFragment()
                else -> ThreeFragment()
            }
        }

        override fun getCount(): Int {
            return 3
        }
    }

}
