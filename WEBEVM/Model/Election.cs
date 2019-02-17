using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Model
{
    public class Election:Entity
    {
        public string Name { get; set; }
        public DateTime StartTime { get; set; }

        //in miliseconds
        public int NominationDuration { get; set; }
        //in miliseconds
        public int VoteDuration { get; set; }
        public virtual ICollection<User> Voter { get; set; }
        [ForeignKey("Voter")]
        public virtual ICollection<string> VoterId { get; set; }
        public virtual ICollection<Nominee> Nominee { get; set; }
        [ForeignKey("Nominee")]
        public virtual ICollection<string> NomineeId { get; set; }
        
    }
}
