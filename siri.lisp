(require "syntax1.lisp")

(defun print-line (str)
  (princ str)
  (terpri)
)

(defun concat (stringA stringB)
  (concatenate 'string stringA stringB)
)

(defun parse-to-google (q)
  (if (string= (subseq q 0 6) "google")
      T
    nil)
)

(defun initiate-siri ()

  (setq query "initial")
  (loop while (not (equal query "exit")) do
	(print-line "Hello how may I help you?")
	(setq query (string-downcase(read-line)))
	;; handle a simple google <x> request
	(if (parse-to-google query)
	 (trivial-shell:shell-command (concat "python search.py " query)))
	 
  )
)