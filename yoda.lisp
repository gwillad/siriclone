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
  (read-from-string
    (concatenate 'string "(" (substitute-if #\space #'punctuation-p
                                            (read-line))
                 ")")))

(defun punctuation-p (char) (find char ".,;:`!?#-()\\\""))

;;; ==============================

(defun yoda ()
  "Respond to user input using pattern matching rules."
  (loop
    (print 'yoda>)
    (let* ((input (read-line-no-punct))
           (response (flatten (use-eliza-rules input))))
      (print-with-spaces response)
      (if (equal response '(good bye)) (RETURN)))))

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
     (How do you do.  Your problem please state.))
    (((?* ?x) computer (?* ?y))
     (Do computers worry you?) (What think you about machines?)
     (Why mention you computers?)
     (What think you machines have to do with your problem?))
    (((?* ?x) name (?* ?y))
     (Interested in names I am not))
    (((?* ?x) sorry (?* ?y))
     (Apologize do not) (Not necessary apologies are)
     (What feelings have you when apologizing you are?))
    (((?* ?x) I remember (?* ?y)) 
     (Often think of ?y do you?)
     (To your mind does thinking of ?y bring anything else?)
     (What else remember do you) (Why recall you ?y right now?))
    (((?* ?x) do you remember (?* ?y))
     (Forget ?y I did  you think?)
     (Why think you I should recall ?y now))

    ;; some new rules
    (((?* ?x) patience (?* ?y))
     (patience you must have young padawan))
    (((?* ?x) believe (?* ?y))
     (that is why you fail))
    (((?* ?x) scared (?* ?y))
     (fear leads to anger  anger leads to hate  hate leads to suffering))
    (((?* ?x) try (?* ?y))
     (do or do not there is no try))
    (((?* ?x) everyone (?* ?y))
     (in absolutes  do only the sith deal))
    
    (((?* ?x) I dreamt (?* ?y))
     (Ever fantasized ?y while you were awake  have you?)
     (Dreamt before ?y have you?))
    (((?* ?x) dream about (?* ?y))
     (How feel you about ?y in reality?))
    (((?* ?x) dream (?* ?y))    
     (To you this dream does what?)
     (Believe that dream has to do with your problem  do you not?))
    (((?* ?x) my mother (?* ?y))
     (About your family tell me more))
    (((?* ?x) my father (?* ?y))
     (Influence you strongly  does he?) 
     (To mind what else comes  hmm when you think of your father?))
    
    (((?* ?x) I want (?* ?y))     
     (Why want you ?y hmmm?))
    (((?* ?x) I am glad (?* ?y))
     (How  helped you to be ?y  have I?) (You happy what makes?))
    (((?* ?x) I am sad (?* ?y))
     (Sorry to hear you are depressed  I am))
    (((?* ?x) are like (?* ?y))   
     (Seen what resemblance between ?x and ?y have you?))
    (((?* ?x) is like (?* ?y))    
     (?x like ?y in what way is?))


    (((?* ?x) I was (?* ?y))       
     (really  were you?) (you were ?y   I already knew))
    (((?* ?x) was I (?* ?y))
     (you were ?y what if?) (you were ?y   do you think?))
    (((?* ?x) I am (?* ?y))
     (are you ?y   how?) (?y do you want to be?))
    (((?* ?x) am I (?* ?y))
     (believe you are ?y   do you) (want to be ?y   do you?))


    (((?* ?x) because (?* ?y))
     (the real reason  is this?) (explain more  does this reason?))
    (((?* ?x) I can't (?* ?y))    
     (?y now  maybe you could))
    (((?* ?x) I feel (?* ?y))     
     (often feel ?y   do you?))
    (((?* ?x) I felt (?* ?y))     
     (other feelings  do you have?))
    (((?* ?x) I (?* ?y) you (?* ?z))   
     (in your fantasy we ?y each other  perhaps))
    (((?* ?x) yes (?* ?y))
     (quite positive  you seem))

    (((?* ?x) someone (?* ?y))
     (More specific  can you be?))
    (((?* ?x) what (?* ?y))
     (you really want to know  what is it?) (think  what do you?))
    (((?* ?x) perhaps (?* ?y))    
     (uncertain you seem))
    (((?* ?x) are (?* ?y))
     (?y  they may be?))
    (((?* ?x)) (fail)))) ;; failure case. allows us to know we failed



(yoda)