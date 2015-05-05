(require "syntax1.lisp")

(defun print-line (str)
  (princ str)
  (terpri)
)

(defun concat (stringA stringB)
  (concatenate 'string stringA stringB)
)

(defun initiate-siri ()
  (print-line "Hello how may I help you?")
  (setq query "initial")
  (loop while (not (equal query "exit")) do
	 (setq query (read-line))
	 (trivial-shell:shell-command (concat "python search.py " query))
  )
)