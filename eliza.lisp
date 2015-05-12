;;; -*- Mode: Lisp; Syntax: Common-Lisp; -*-
;;; Code from Paradigms of Artificial Intelligence Programming
;;; Copyright (c) 1991 Peter Norvig

;;;; File eliza.lisp: Advanced version of Eliza.
;;; Has more rules, and accepts input without parens.

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

(defun eliza ()
  "Respond to user input using pattern matching rules."
  (loop
    (print 'eliza>)
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

(defparameter *siri-rules* 
  '(((google (?* ?x))
     (Please let me google that for you))))
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
     (To mind does thinking of ?y bring anything elsee?)
    (What else remember do you) (Why recall you ?y right now?))
   (((?* ?x) do you remember (?* ?y))
    (Forget ?y I did you think?)
    (Why think you I should recall ?y now))

   (((?* ?x) I dreamt (?* ?y))
    (Ever fantasized ?y while you were awake have you?)
    (Dream blank before ?y have you?))
   (((?* ?x) dream about (?* ?y))
    (How feel you about ?y in reality?))
   (((?* ?x) dream (?* ?y))    
    (To you this dream does what?)
    (Believe that dream has to do with your problem do you not?))
   (((?* ?x) my mother (?* ?y))
    (About your family tell me more))
   (((?* ?x) my father (?* ?y))
    (Influence you strongly does he?) 
    (To mind what else comes hmm when you think of your father?))

   (((?* ?x) I want (?* ?y))     
    (Why want you ?y hmmm?))
   (((?* ?x) I am glad (?* ?y))
    (How helped you to be ?y have I?) (You happy what makes?))
   (((?* ?x) I am sad (?* ?y))
    (Sorry to hear you are depressed I am))
   (((?* ?x) are like (?* ?y))   
    (Seen what resemblance between ?x and ?y have you?))
   (((?* ?x) is like (?* ?y))    
    (?x like ?y in what way is?))

   (((?* ?x) I was (?* ?y))       
    (Were you really?) (Perhaps I already knew you were ?y)
    (Why do you tell me you were ?y now?))
   (((?* ?x) was I (?* ?y))
    (What if you were ?y ?) (Do you thin you were ?y)
    (What would it mean if you were ?y))
   (((?* ?x) I am (?* ?y))       
    (In what way are you ?y) (Do you want to be ?y ?))
   (((?* ?x) am I (?* ?y))
    (Do you believe you are ?y) (Would you want to be ?y)
    (You wish I would tell you you are ?y)
    (What would it mean if you were ?y))
   (((?* ?x) am (?* ?y))
    (Why do you say "AM?") (I don't understand that))
   (((?* ?x) are you (?* ?y))
    (Why are you interested in whether I am ?y or not?)
    (Would you prefer if I weren't ?y)
    (Perhaps I am ?y in your fantasies))
   (((?* ?x) you are (?* ?y))   
    (What makes you think I am ?y ?))

   (((?* ?x) because (?* ?y))
    (Is that the real reason?) (What other reasons might there be?)
    (Does that reason seem to explain anything else?))
   (((?* ?x) were you (?* ?y))
    (Perhaps I was ?y) (What do you think?) (What if I had been ?y))
   (((?* ?x) I can't (?* ?y))    
    (Maybe you could ?y now) (What if you could ?y ?))
   (((?* ?x) I feel (?* ?y))     
    (Do you often feel ?y ?))
   (((?* ?x) I felt (?* ?y))     
    (What other feelings do you have?))
   (((?* ?x) I (?* ?y) you (?* ?z))   
    (Perhaps in your fantasy we ?y each other))
   (((?* ?x) why don't you (?* ?y))
    (Should you ?y yourself?)
    (Do you believe I don't ?y) (Perhaps I will ?y in good time))
   (((?* ?x) yes (?* ?y))
    (You seem quite positive) (You are sure) (I understand))
   (((?* ?x) no (?* ?y))
    (Why not?) (You are being a bit negative)
    (Are you saying "NO" just to be negative?))

   (((?* ?x) someone (?* ?y))
    (Can you be more specific?))
   (((?* ?x) everyone (?* ?y))
    (surely not everyone) (Can you think of anyone in particular?)
    (Who for example?) (You are thinking of a special person))
   (((?* ?x) always (?* ?y))
    (Can you think of a specific example) (When?)
    (What incident are you thinking of?) (Really-- always))
   (((?* ?x) what (?* ?y))
    (Why do you ask?) (Does that question interest you?)
    (What is it you really want to know?) (What do you think?)
    (What comes to your mind when you ask that?))
   (((?* ?x) perhaps (?* ?y))    
    (You do not seem quite certain))
   (((?* ?x) are (?* ?y))
    (Did you think they might not be ?y)
    (Possibly they are ?y))
   (((?* ?x)) (fail)              
    ;(Very interesting) (I am not sure I understand you fully)
    ;(What does that suggest to you?) (Please continue) (Go on) 
    ;(Do you feel strongly about discussing such things?))))
)))
;;; ==============================

(eliza)