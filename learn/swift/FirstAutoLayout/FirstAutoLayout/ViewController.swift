//
//  ViewController.swift
//  FirstAutoLayout
//
//  Created by Jaedoo Ko on 2019/10/27.
//  Copyright © 2019 Jaedoo Ko. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet var label:UILabel!
    @IBOutlet var button:UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        button.translatesAutoresizingMaskIntoConstraints = false
        var constraintX:NSLayoutConstraint
        var constraintY:NSLayoutConstraint
        constraintX = button.centerXAnchor.constraint(equalTo: self.view.centerXAnchor)
        constraintY = button.centerYAnchor.constraint(equalTo: self.view.centerYAnchor)
        constraintX.isActive = true
        constraintY.isActive = true
        
        label.translatesAutoresizingMaskIntoConstraints = false
        var buttonConstraintX:NSLayoutConstraint
        var topConstraint:NSLayoutConstraint
        buttonConstraintX = label.centerXAnchor.constraint(equalTo: button.centerXAnchor)
        topConstraint = label.bottomAnchor.constraint(equalTo: button.topAnchor, constant: -10)
        buttonConstraintX.isActive = true
        topConstraint.isActive = true
        
        var widthConstraint:NSLayoutConstraint
        widthConstraint = label.widthAnchor.constraint(equalTo: button.widthAnchor, multiplier: 2.0)
        widthConstraint.isActive = true
        
        label.backgroundColor = UIColor.brown
        button.backgroundColor = UIColor.blue
        
        
    }

    
    
    

}

