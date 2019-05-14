package com.myproject.myapplication

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.support.v4.app.Fragment
import android.support.v4.app.FragmentManager
import android.support.v4.app.FragmentStatePagerAdapter
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        pager.adapter = MyPagerAdapter(supportFragmentManager)
        pager.currentItem = 0

        movePageListener =

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
