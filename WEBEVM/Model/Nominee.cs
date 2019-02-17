using System.ComponentModel.DataAnnotations.Schema;

namespace Model
{
    public class Nominee:Entity
    {
        public string UserId { get; set; }
        public int PresidentVoteCount { get; set; }
        public int VicePresidentVoteCount { get; set; }
        public int SecretaryVoteCount { get; set; }
    }
}
