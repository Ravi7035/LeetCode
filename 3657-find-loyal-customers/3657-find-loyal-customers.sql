select customer_id 
from customer_transactions
group by customer_id
having count(transaction_id) >=3 and datediff(Max(transaction_date),Min(transaction_date))>=30 and ((sum(
    case
        when transaction_type="refund" then 1
        else 0

    end
) / count(transaction_type)) * 100 ) < 20


