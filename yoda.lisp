;;; -*- Mode: Lisp; Syntax: Common-Lisp; -*-
;;; Code from Paradigms of Artificial Intelligence Programming
;;; Copyright (c) 1991 Peter Norvig

;;;; File eliza.lisp: Advanced version of Eliza.
;;; Has more rules, and accepts input without parens.

;;modified by Casey Collins and Adam Gwilliam

(load "auxfns")
(requires "eliza1")

;;; ==============================

(defun read-line-no-punct ()
  "Read an input line, ignoring punctuation."
  ;; ERROR: reduces fractions, making dates like 5/15 impossible. 
  (read-from-string
    (concatenate 'string "(" (substitute-if #\space #'punctuation-p
                                            (read-line))
                 ")")))

(defun punctuation-p (char) (find char ".,;:`!?#-()\\\""))

;;; ==============================

(defun concat (stringA stringB)
  (concatenate 'string stringA stringB)
)

(defun concat-all (str lst)
  (if (null lst) str
  (concat-all (concat str (concat " " (write-to-string (car lst)))) (cdr lst)))
)

(defun siri ()
  "Respond to user input using pattern matching rules."
  (loop
    (print 'siri>)
    (let* ((input (read-line-no-punct))
           (response (flatten (use-eliza-rules input))))
      (if (equal (first response) 'api_weather) (trivial-shell:shell-command (concat-all  "python apis/weather.py" (cdr response))))
      (if (equal (first response) 'gen_response) (print-with-spaces (cdr response)))
      (if (equal (first response) 'nothing_matched) (trivial-shell:shell-command (concat-all "python apis/wolfram/wolfram_questions.py" input)))
      (if (equal (first response) 'add) (trivial-shell:shell-command (concat-all "python2.7 apis/contacts/contacts.py" response)))
      (if (equal (first response) 'call) (trivial-shell:shell-command (concat-all "python2.7 apis/contacts/contacts.py" response)))
      (if (equal (first response) 'text) (trivial-shell:shell-command (concat-all "python2.7 apis/contacts/contacts.py" response)))
      (if (equal (first response) 'email) (trivial-shell:shell-command (concat-all "python2.7 apis/contacts/contacts.py" response)))
      (if (equal (first response) 'exit_siri) (RETURN)))))


(defun print-with-spaces (list)
  (mapc #'(lambda (x) (prin1 x) (princ " ")) list))

(defun print-with-spaces (list)
  (format t "~{~a ~}" list))

;;; ==============================

(defun mappend (fn &rest lists)	
  "Apply fn to each element of lists and append the results."
  (apply #'append (apply #'mapcar fn lists)))

;;; ==============================

(defparameter *eliza-rules*
  '((((?* ?x) hello (?* ?y))      
     (gen_response Greetings. My name is Siri. What can I do for you ))
    (((?* ?a) weather (?* ?x)) (api_weather ?x))
    ((exit) (exit_siri))
    ((Add (?* ?x) to my contacts) (add ?x))
    ((Add contact) (add))
    ((add) (add))
    ((Add (?* ?x)) (add ?x))
    ((Add contact (?* ?x)) (add ?x))
    (((?* ?y) Call (?* ?x)) (call ?x))
    (((?* ?y) text (?* ?x)) (text ?x))
    (((?* ?y) email (?* ?x)) (email ?x))
    (((?* ?y) view (?* ?x)) (view ?x))
    ((Call (?* ?x)) (call ?x))
    ((text (?* ?x)) (text ?x))
    ((email (?* ?x)) (email ?x))
    ((view (?* ?x)) (view ?x))
    (((?* ?x)) (nothing_matched)))) ;; failure case. allows us to know we failed
