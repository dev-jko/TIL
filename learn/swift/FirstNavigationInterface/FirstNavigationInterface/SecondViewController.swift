//
//  SecendViewController.swift
//  FirstNavigationInterface
//
//  Created by Jaedoo Ko on 2019/10/28.
//  Copyright © 2019 Jaedoo Ko. All rights reserved.
//

import UIKit

class SecondViewController: UIViewController {

    
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }
    
    @IBAction func popToPrev() {
        self.navigationController?.popViewController(animated: true)
    }
}
